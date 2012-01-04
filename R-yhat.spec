%global packname  yhat
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Interpreting Regression Effects

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MBESS R-yacca 

BuildRequires:    R-devel tex(latex) R-MBESS R-yacca 

%description
The purpose of this package is to provide methods for variance
partitioning for linear models and canonical correlation and methods for
interpreting regression effects using beta weights, standardized beta
weights, structure coefficients, and adjusted effect sizes.

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
%doc %{rlibdir}/yhat/html
%doc %{rlibdir}/yhat/DESCRIPTION
%{rlibdir}/yhat/Meta
%{rlibdir}/yhat/INDEX
%{rlibdir}/yhat/R
%{rlibdir}/yhat/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora