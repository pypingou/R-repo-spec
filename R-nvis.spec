%global packname  nvis
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Combination of visualization functions for nuclear data using ggplot2 and ggcolpairs.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ggplot2 R-ggcolpairs 

BuildRequires:    R-devel tex(latex) R-ggplot2 R-ggcolpairs 

%description
The nvis package facilitates the visualization of nuclear data with
customized functions using ggplot2.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora