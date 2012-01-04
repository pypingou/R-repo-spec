%global packname  candisc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.19
Release:          1%{?dist}
Summary:          Generalized Canonical Discriminant Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-19.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-car R-heplots R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-car R-heplots R-graphics R-stats 

%description
Functions for computing and graphing canonical discriminant analyses.

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
%doc %{rlibdir}/candisc/NEWS
%doc %{rlibdir}/candisc/html
%doc %{rlibdir}/candisc/DESCRIPTION
%{rlibdir}/candisc/Meta
%{rlibdir}/candisc/R
%{rlibdir}/candisc/data
%{rlibdir}/candisc/help
%{rlibdir}/candisc/NAMESPACE
%{rlibdir}/candisc/demo
%{rlibdir}/candisc/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.19-1
- initial package for Fedora