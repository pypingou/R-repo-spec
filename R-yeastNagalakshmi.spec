%global packname  yeastNagalakshmi
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99.3
Release:          1%{?dist}
Summary:          Yeast genome RNA sequencing data based on Nagalakshmi et. al.

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The yeast genome data was retrieved from the sequence read archive,
aligned with bwa, and converted to BAM format with samtools.

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
%doc %{rlibdir}/yeastNagalakshmi/DESCRIPTION
%doc %{rlibdir}/yeastNagalakshmi/html
%{rlibdir}/yeastNagalakshmi/INDEX
%{rlibdir}/yeastNagalakshmi/NAMESPACE
%{rlibdir}/yeastNagalakshmi/help
%{rlibdir}/yeastNagalakshmi/extdata
%{rlibdir}/yeastNagalakshmi/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.3-1
- initial package for Fedora