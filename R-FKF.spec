%global packname  FKF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Fast Kalman Filter

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This is a fast and flexible implementation of the Kalman filter, which can
deal with NAs. It is entirely written in C and relies fully on linear
algebra subroutines contained in BLAS and LAPACK. Due to the speed of the
filter, the fitting of high-dimensional linear state space models to large
datasets becomes possible. This package also contains a plot function for
the visualization of the state vector and graphical diagnostics of the

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
%doc %{rlibdir}/FKF/DESCRIPTION
%doc %{rlibdir}/FKF/html
%{rlibdir}/FKF/NAMESPACE
%{rlibdir}/FKF/unitTests
%{rlibdir}/FKF/libs
%{rlibdir}/FKF/INDEX
%{rlibdir}/FKF/R
%{rlibdir}/FKF/Meta
%{rlibdir}/FKF/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora