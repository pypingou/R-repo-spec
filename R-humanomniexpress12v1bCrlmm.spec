%global packname  humanomniexpress12v1bCrlmm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Metadata for fast genotyping with the 'crlmm' package

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-utils 


%description
Package with metadata for genotyping Illumina Omni Express 12 arrays using
the 'crlmm' package.

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
%doc %{rlibdir}/humanomniexpress12v1bCrlmm/DESCRIPTION
%doc %{rlibdir}/humanomniexpress12v1bCrlmm/html
%{rlibdir}/humanomniexpress12v1bCrlmm/NAMESPACE
%{rlibdir}/humanomniexpress12v1bCrlmm/extdata
%{rlibdir}/humanomniexpress12v1bCrlmm/Meta
%{rlibdir}/humanomniexpress12v1bCrlmm/R
%{rlibdir}/humanomniexpress12v1bCrlmm/INDEX
%{rlibdir}/humanomniexpress12v1bCrlmm/help
RPM build errors:

%changelog
* Wed Dec 07 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora