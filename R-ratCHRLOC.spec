%global packname  ratCHRLOC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.6
Release:          1%{?dist}
Summary:          A data package containing annotation data for ratCHRLOC

Group:            Applications/Engineering 
License:          The Artistic License, Version 2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Annotation data file for ratCHRLOC assembled using data from public data

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
%doc %{rlibdir}/ratCHRLOC/DESCRIPTION
%doc %{rlibdir}/ratCHRLOC/html
%{rlibdir}/ratCHRLOC/Meta
%{rlibdir}/ratCHRLOC/help
%{rlibdir}/ratCHRLOC/R
%{rlibdir}/ratCHRLOC/INDEX
%{rlibdir}/ratCHRLOC/data
%{rlibdir}/ratCHRLOC/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.6-1
- initial package for Fedora