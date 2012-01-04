%global packname  RMAPPER
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          R interface to the MAPPER database of transcription factor binding sites

Group:            Applications/Engineering 
License:          Artistic 2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
The RMAPPER package allows you to retrieve a set of predicted
transcription factor binding sites from the MAPPER database
(http://genome.ufl.edu/mapper/) through a simple HTTP request.

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
%doc %{rlibdir}/RMAPPER/doc
%doc %{rlibdir}/RMAPPER/html
%doc %{rlibdir}/RMAPPER/DESCRIPTION
%{rlibdir}/RMAPPER/Meta
%{rlibdir}/RMAPPER/NAMESPACE
%{rlibdir}/RMAPPER/INDEX
%{rlibdir}/RMAPPER/R
%{rlibdir}/RMAPPER/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora