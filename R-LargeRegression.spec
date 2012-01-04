%global packname  LargeRegression
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Large Regressions

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Matrix 

%description
Uses gradient descent to minimize the sum of squared residuals for the
regression problem.  Can include an L2 penalty on the coefficient matrix.
This function is very useful when there is an initial guess of what B
should be in Y = XB. In general, this function performs faster than R's lm
function. GPU acceleration can be used to make this function extremely
fast.  This package suggests cudaMatrixOps, which is not on CRAN but can
be downloaded at stanford.edu/~jeffwong.

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
%doc %{rlibdir}/LargeRegression/DESCRIPTION
%doc %{rlibdir}/LargeRegression/html
%{rlibdir}/LargeRegression/INDEX
%{rlibdir}/LargeRegression/Meta
%{rlibdir}/LargeRegression/R
%{rlibdir}/LargeRegression/NAMESPACE
%{rlibdir}/LargeRegression/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora