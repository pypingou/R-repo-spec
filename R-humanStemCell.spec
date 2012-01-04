%global packname  humanStemCell
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          Human Stem Cells time course experiment

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase R-hgu133plus2.db 

BuildRequires:    R-devel tex(latex) R-Biobase R-hgu133plus2.db 

%description
Affymetrix time course experiment on human stem cells (two time points:
undifferentiated and differentiated).

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.5-1
- initial package for Fedora