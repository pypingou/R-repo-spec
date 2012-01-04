%global packname  mAr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Multivariate AutoRegressive analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
R functions for multivariate autoregressive analysis

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
%doc %{rlibdir}/mAr/html
%doc %{rlibdir}/mAr/DESCRIPTION
%{rlibdir}/mAr/NAMESPACE
%{rlibdir}/mAr/Meta
%{rlibdir}/mAr/INDEX
%{rlibdir}/mAr/R
%{rlibdir}/mAr/help
%{rlibdir}/mAr/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora