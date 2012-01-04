%global packname  fisheyeR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          Fisheye and Hyperbolic-space-alike Interactive Visualization Tools in R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tkrplot R-methods 

BuildRequires:    R-devel tex(latex) R-tkrplot R-methods 

%description
fisheyeR provides tools for creating Interactive Data Visualizations by
implementing ideas from Furnas, Munzner, Costa and Venturini.

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
%doc %{rlibdir}/fisheyeR/html
%doc %{rlibdir}/fisheyeR/DESCRIPTION
%{rlibdir}/fisheyeR/Meta
%{rlibdir}/fisheyeR/INDEX
%{rlibdir}/fisheyeR/R
%{rlibdir}/fisheyeR/NAMESPACE
%{rlibdir}/fisheyeR/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9-1
- initial package for Fedora