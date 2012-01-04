%global packname  gafit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Genetic Algorithm for Curve Fitting

Group:            Applications/Engineering 
License:          GPL version 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A group of sample points are evaluted against a user-defined expression,
the sample points are lists of parameters with values that may be
substituted into that expression. The genetic algorithm attmepts to make
the result of the expression as low as possible (usually this would be the
sum of residuals squared).

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
%doc %{rlibdir}/gafit/DESCRIPTION
%doc %{rlibdir}/gafit/html
%{rlibdir}/gafit/NAMESPACE
%{rlibdir}/gafit/R
%{rlibdir}/gafit/INDEX
%{rlibdir}/gafit/help
%{rlibdir}/gafit/libs
%{rlibdir}/gafit/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.1-1
- initial package for Fedora