%global packname  cosmoGUI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          GUI for constructing constraint sets used by the cosmo package

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tkWidgets R-cosmo 


BuildRequires:    R-devel tex(latex) R-tkWidgets R-cosmo



%description
cosmoGUI allows the user to interactively define constraint sets that can
be used by the cosmo package to supervise the search for shared motifs in
a set of DNA sequences. The constraints can be either adapted from a set
of commonly used templates or defined from scratch.

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
%doc %{rlibdir}/cosmoGUI/DESCRIPTION
%doc %{rlibdir}/cosmoGUI/html
%{rlibdir}/cosmoGUI/R
%{rlibdir}/cosmoGUI/NAMESPACE
%{rlibdir}/cosmoGUI/help
%{rlibdir}/cosmoGUI/INDEX
%{rlibdir}/cosmoGUI/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora