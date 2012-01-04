%global packname  stratigraph
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.64
Release:          1%{?dist}
Summary:          Toolkit for the plotting and analysis of stratigraphic and palaeontological data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid 

BuildRequires:    R-devel tex(latex) R-grid 

%description
A collection of tools for plotting and analyzing paleontological and
geological data distributed through through time in stratigraphic cores or
sections. Includes some miscellaneous functions for handling other kinds
of palaeontological and paleoecological data.

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
%doc %{rlibdir}/stratigraph/html
%doc %{rlibdir}/stratigraph/DESCRIPTION
%{rlibdir}/stratigraph/INDEX
%{rlibdir}/stratigraph/NAMESPACE
%{rlibdir}/stratigraph/R
%{rlibdir}/stratigraph/data
%{rlibdir}/stratigraph/Meta
%{rlibdir}/stratigraph/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.64-1
- initial package for Fedora