%global packname  desirability
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.03
Release:          1%{dist}
Summary:          Desirabiliy Function Optimization and Ranking

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
S3 classes for multivariate optimization using the desirability function
by Derringer and Suich (1980)

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/desirability/html
%doc %{rlibdir}/desirability/NEWS
%doc %{rlibdir}/desirability/DESCRIPTION
%doc %{rlibdir}/desirability/doc
%{rlibdir}/desirability/INDEX
%{rlibdir}/desirability/R
%{rlibdir}/desirability/NAMESPACE
%{rlibdir}/desirability/help
%{rlibdir}/desirability/Meta

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.03-1
- Update to version 1.03

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.03-1
- initial package for Fedora