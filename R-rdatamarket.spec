%global packname  rdatamarket
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.3
Release:          1%{?dist}
Summary:          Data access API for DataMarket.com

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-zoo 
Requires:         R-RCurl R-RJSONIO 

BuildRequires:    R-devel tex(latex) R-zoo
BuildRequires:    R-RCurl R-RJSONIO 


%description
Fetches data from DataMarket.com, either as timeseries in zoo form
(dmseries) or as long-form data frames (dmlist). Metadata including
dimension structure is fetched with dminfo, or just the dimensions with

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.3-1
- initial package for Fedora