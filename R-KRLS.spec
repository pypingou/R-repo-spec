%global packname  KRLS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{dist}
Summary:          Kernel-based Regularized Least Squares (KRLS)

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Package implements Kernel-based Regularized Least Squares (KRLS), a
machine learning method that can be used to fit multidimensional functions
for regression and classification problems without relying on linearity or
additivity assumptions. This package is currently in alpha phase (feedback
is appreciated).

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
%doc %{rlibdir}/KRLS/html
%doc %{rlibdir}/KRLS/DESCRIPTION
%{rlibdir}/KRLS/R
%{rlibdir}/KRLS/help
%{rlibdir}/KRLS/INDEX
%{rlibdir}/KRLS/Meta
%{rlibdir}/KRLS/NAMESPACE
%{rlibdir}/KRLS/LICENSE

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- Update to version 0.2

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora