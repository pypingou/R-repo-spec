%global packname  hapmap370k
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Example Illumina 370k HapMap Data

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Example HapMap data from Illumina 370k BeadChips

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
%doc %{rlibdir}/hapmap370k/CITATION
%doc %{rlibdir}/hapmap370k/DESCRIPTION
%doc %{rlibdir}/hapmap370k/html
%{rlibdir}/hapmap370k/idatFiles
%{rlibdir}/hapmap370k/NAMESPACE
%{rlibdir}/hapmap370k/R
%{rlibdir}/hapmap370k/Meta
%{rlibdir}/hapmap370k/INDEX
%{rlibdir}/hapmap370k/help

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora