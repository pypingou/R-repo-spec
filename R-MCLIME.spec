%global packname  MCLIME
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Simultaneous Estimation of the Regression Coefficients and Precision Matrix

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lpSolve 

BuildRequires:    R-devel tex(latex) R-lpSolve 

%description
A robust constrained L1 minimization method for estimating the regression
coefficients and a large sparse inverse covariance matrix (i.e. precision
matrix) simultaneoulsy. The computation uses linear programming.

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
%doc %{rlibdir}/MCLIME/html
%doc %{rlibdir}/MCLIME/DESCRIPTION
%{rlibdir}/MCLIME/INDEX
%{rlibdir}/MCLIME/Meta
%{rlibdir}/MCLIME/NAMESPACE
%{rlibdir}/MCLIME/help
%{rlibdir}/MCLIME/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora