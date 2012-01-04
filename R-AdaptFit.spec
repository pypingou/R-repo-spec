%global packname  AdaptFit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Adaptive Semiparametic Regression

Group:            Applications/Engineering 
License:          GPL (version 2 or later)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-SemiPar R-MASS R-nlme R-cluster 

BuildRequires:    R-devel tex(latex) R-SemiPar R-MASS R-nlme R-cluster 

%description
Based on the function "spm" of the SemiPar package fits semiparametric
regression models with spatially adaptive penalized splines.

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
%doc %{rlibdir}/AdaptFit/html
%doc %{rlibdir}/AdaptFit/DESCRIPTION
%{rlibdir}/AdaptFit/data
%{rlibdir}/AdaptFit/help
%{rlibdir}/AdaptFit/Meta
%{rlibdir}/AdaptFit/INDEX
%{rlibdir}/AdaptFit/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2-1
- initial package for Fedora