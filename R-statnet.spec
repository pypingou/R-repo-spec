%global packname  statnet
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.6
Release:          1%{?dist}
Summary:          Software tools for the Statistical Modeling of Network Data

Group:            Applications/Engineering 
License:          GPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-network R-ergm R-latentnet R-degreenet R-sna R-abind R-shapes R-tools R-utils 


BuildRequires:    R-devel tex(latex) R-network R-ergm R-latentnet R-degreenet R-sna R-abind R-shapes R-tools R-utils



%description
An integrated set of tools for the representation, visualization, analysis
and simulation of network data. For an introduction type:

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6-1
- initial package for Fedora