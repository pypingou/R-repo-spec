%global packname  MEEBOdata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          MEEBO set and MEEBO controls.

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
R objects describing the MEEBO set.

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
%doc %{rlibdir}/MEEBOdata/html
%doc %{rlibdir}/MEEBOdata/DESCRIPTION
%{rlibdir}/MEEBOdata/help
%{rlibdir}/MEEBOdata/INDEX
%{rlibdir}/MEEBOdata/data
%{rlibdir}/MEEBOdata/Meebo
%{rlibdir}/MEEBOdata/NAMESPACE
%{rlibdir}/MEEBOdata/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora