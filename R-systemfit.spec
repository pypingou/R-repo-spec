%global packname  systemfit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.10
Release:          1%{?dist}
Summary:          Estimating Systems of Simultaneous Equations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix R-car R-lmtest 

BuildRequires:    R-devel tex(latex) R-Matrix R-car R-lmtest 

%description
This package contains functions for fitting simultaneous systems of linear
and nonlinear equations using Ordinary Least Squares (OLS), Weighted Least
Squares (WLS), Seemingly Unrelated Regressions (SUR), Two-Stage Least
Squares (2SLS), Weighted Two-Stage Least Squares (W2SLS), and Three-Stage
Least Squares (3SLS).

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
%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.10-1
- initial package for Fedora