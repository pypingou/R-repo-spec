%global packname  iontreeData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99.5
Release:          1%{?dist}
Summary:          Data provided to show the usage of functions in iontree package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Raw MS2, MS3 scans from direct infusion mass spectrometry (DIMS) and a
demo ion tree database 'mzDB' derived from the DIMS data are included. The
demo database is used to show the functionalities provided by the
'iontree' package, not for the purpose of compound identification by any

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
%doc %{rlibdir}/iontreeData/DESCRIPTION
%doc %{rlibdir}/iontreeData/html
%{rlibdir}/iontreeData/NAMESPACE
%{rlibdir}/iontreeData/db
%{rlibdir}/iontreeData/INDEX
%{rlibdir}/iontreeData/help
%{rlibdir}/iontreeData/data
%{rlibdir}/iontreeData/mzxml
%{rlibdir}/iontreeData/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.5-1
- initial package for Fedora