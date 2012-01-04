%global packname  ecoliLeucine
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.7
Release:          1%{?dist}
Summary:          Experimental data with Affymetrix E. coli chips

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-affy R-ecolicdf 


BuildRequires:    R-devel tex(latex) R-affy R-ecolicdf



%description
Experimental data with Affymetrix E. coli chips, as reported in She-pin
Hung, Pierre Baldi, and G. Wesley Hatfield, J. Biol. Chem., Vol. 277,
Issue 43, 40309-40323, October 25, 2002

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.7-1
- initial package for Fedora