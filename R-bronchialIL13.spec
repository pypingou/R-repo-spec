%global packname  bronchialIL13
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          time course experiment involving il13

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-affy 


BuildRequires:    R-devel tex(latex) R-affy



%description
derived from CNMC (pepr.cnmcresearch.org)
http://pepr.cnmcresearch.org/browse.do?action=list_prj_exp&projectId=95
Human Bronchial Cell line A549

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.8-1
- initial package for Fedora