%global packname  delftfews
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.136
Release:          1%{?dist}
Summary:          delftfews R extensions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-136.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-XML R-logging R-zoo R-methods 

BuildRequires:    R-devel tex(latex) R-XML R-logging R-zoo R-methods 

%description
a collection of timeseries sets handling functions used here at work
(Nelen en Schuurmans), initially for the Lizard Scripter.

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
%doc %{rlibdir}/delftfews/DESCRIPTION
%doc %{rlibdir}/delftfews/html
%{rlibdir}/delftfews/R
%{rlibdir}/delftfews/INDEX
%{rlibdir}/delftfews/unitTest
%{rlibdir}/delftfews/help
%{rlibdir}/delftfews/NAMESPACE
%{rlibdir}/delftfews/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.136-1
- initial package for Fedora