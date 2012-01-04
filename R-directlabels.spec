%global packname  directlabels
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Direct labels for multicolor plots in lattice or ggplot2

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid 

BuildRequires:    R-devel tex(latex) R-grid 

%description
The directlabels package provides an extensible framework for
automatically placing direct labels onto multicolor lattice or ggplot2
plots. It includes heuristics for examining "lattice" and "ggplot" objects
and inferring an appropriate Positioning Method for placing the labels.
Furthermore, the design of directlabels makes it simple to create
Positioning Methods for specific plots or libraries of portable
Positioning Methods that can be re-used.

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
%doc %{rlibdir}/directlabels/html
%doc %{rlibdir}/directlabels/DESCRIPTION
%doc %{rlibdir}/directlabels/NEWS
%{rlibdir}/directlabels/Meta
%{rlibdir}/directlabels/data
%{rlibdir}/directlabels/R
%{rlibdir}/directlabels/NAMESPACE
%{rlibdir}/directlabels/help
%{rlibdir}/directlabels/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora