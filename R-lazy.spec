%global packname  lazy
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.14
Release:          1%{?dist}
Summary:          Lazy Learning for Local Regression

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
By combining constant, linear, and quadratic local models, lazy estimates
the value of an unknown multivariate function on the basis of a set of
possibly noisy samples of the function itself. This implementation of lazy
learning automatically adjusts the bandwidth on a query-by-query basis
through a leave-one-out cross-validation.

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
%doc %{rlibdir}/lazy/html
%doc %{rlibdir}/lazy/DESCRIPTION
%doc %{rlibdir}/lazy/COPYING
%{rlibdir}/lazy/NAMESPACE
%{rlibdir}/lazy/help
%{rlibdir}/lazy/Meta
%{rlibdir}/lazy/R
%{rlibdir}/lazy/COPYRIGHTS
%{rlibdir}/lazy/libs
%{rlibdir}/lazy/ACKNOWLEDGMENTS
%{rlibdir}/lazy/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.14-1
- initial package for Fedora