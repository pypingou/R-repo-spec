%global packname  MCPMod
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Design and Analysis of Dose-Finding Studies (see also DoseFinding package)

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-lattice 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-lattice 

%description
This package implements a methodology for the design and analysis of
dose-response studies that combines aspects of multiple comparison
procedures and modeling approaches (Bretz, Pinheiro and Branson, 2005,
Biometrics 61, 738-748). The package provides tools for the analysis of
dose finding trials as well as a variety of tools necessary to plan a
trial to be conducted with the MCPMod methodology. ***NOTE*** The MCPMod
package will not be further developed, all future development of the
MCP-Mod methodology will be done in the DoseFinding R-package. ***NOTE***

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
%doc %{rlibdir}/MCPMod/html
%doc %{rlibdir}/MCPMod/DESCRIPTION
%doc %{rlibdir}/MCPMod/NEWS
%doc %{rlibdir}/MCPMod/doc
%doc %{rlibdir}/MCPMod/CITATION
%{rlibdir}/MCPMod/data
%{rlibdir}/MCPMod/R
%{rlibdir}/MCPMod/LICENSE
%{rlibdir}/MCPMod/NAMESPACE
%{rlibdir}/MCPMod/INDEX
%{rlibdir}/MCPMod/README
%{rlibdir}/MCPMod/help
%{rlibdir}/MCPMod/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.7-1
- initial package for Fedora