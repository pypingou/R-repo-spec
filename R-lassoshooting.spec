%global packname  lassoshooting
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.4.4
Release:          1%{?dist}
Summary:          L1 regularized regression (Lasso) solver using the Cyclic Coordinate Descent algorithm aka Lasso Shooting

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1.4-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
L1 regularized regression (Lasso) solver using the Cyclic Coordinate
Descent algorithm aka Lasso Shooting is fast. This implementation can
choose which coefficients to penalize. It support coefficient-specific
penalities and it can take X'X and X'y instead of X and y.

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
%doc %{rlibdir}/lassoshooting/DESCRIPTION
%doc %{rlibdir}/lassoshooting/html
%{rlibdir}/lassoshooting/Meta
%{rlibdir}/lassoshooting/NAMESPACE
%{rlibdir}/lassoshooting/libs
%{rlibdir}/lassoshooting/help
%{rlibdir}/lassoshooting/LICENSE
%{rlibdir}/lassoshooting/R
%{rlibdir}/lassoshooting/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4.4-1
- initial package for Fedora