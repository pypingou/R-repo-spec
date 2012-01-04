%global packname  spikeLI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.14.0
Release:          1%{?dist}
Summary:          Affymetrix Spike-in Langmuir Isotherm Data Analysis Tool

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
SpikeLI  is a package that performs the analysis of the Affymetrix
spike-in data using the Langmuir Isotherm. The aim of this package is to
show the advantages of a physical-chemistry based analysis of the
Affymetrix microarray data compared to the traditional methods. The
spike-in (or Latin square) data for the HGU95 and HGU133 chipsets have
been downloaded from the Affymetrix web site. The model used in the
spikeLI package is described in details in E. Carlon and T. Heim, Physica
A 362, 433 (2006).

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
%doc %{rlibdir}/spikeLI/html
%doc %{rlibdir}/spikeLI/doc
%doc %{rlibdir}/spikeLI/DESCRIPTION
%{rlibdir}/spikeLI/NAMESPACE
%{rlibdir}/spikeLI/Meta
%{rlibdir}/spikeLI/R
%{rlibdir}/spikeLI/demo
%{rlibdir}/spikeLI/data
%{rlibdir}/spikeLI/INDEX
%{rlibdir}/spikeLI/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.14.0-1
- initial package for Fedora