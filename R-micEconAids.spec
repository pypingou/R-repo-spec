%global packname  micEconAids
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.6
Release:          1%{?dist}
Summary:          Demand Analysis with the Almost Ideal Demand System (AIDS)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-systemfit R-miscTools R-lmtest R-micEcon 

BuildRequires:    R-devel tex(latex) R-systemfit R-miscTools R-lmtest R-micEcon 

%description
Demand analysis with the Almost Ideal Demand System (AIDS) suggested by
Deaton and Muellbauer (1980)

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
%doc %{rlibdir}/micEconAids/html
%doc %{rlibdir}/micEconAids/NEWS
%doc %{rlibdir}/micEconAids/DESCRIPTION
%{rlibdir}/micEconAids/NAMESPACE
%{rlibdir}/micEconAids/help
%{rlibdir}/micEconAids/data
%{rlibdir}/micEconAids/Meta
%{rlibdir}/micEconAids/INDEX
%{rlibdir}/micEconAids/R

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.6-1
- initial package for Fedora