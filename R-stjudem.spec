%global packname  stjudem
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.6
Release:          1%{?dist}
Summary:          Microarray Data from Yeoh et al. in MACAT format

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
This is a microarray data set on acute lymphoblastic leukemia, published
in 2002 (Yeoh et al.Cancer Cell 2002). The experiments were conducted in
the St.Jude Children's Research Hospital, Memphis, Tenessee, USA. The raw
data was preprocessed by variance stabilizing normalization (Huber et al.)
on probe and subsequent summarization of probe expression values into
probe set expression values using median polish.

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
%doc %{rlibdir}/stjudem/html
%doc %{rlibdir}/stjudem/DESCRIPTION
%{rlibdir}/stjudem/Meta
%{rlibdir}/stjudem/help
%{rlibdir}/stjudem/data
%{rlibdir}/stjudem/NAMESPACE
%{rlibdir}/stjudem/INDEX
%{rlibdir}/stjudem/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.6-1
- initial package for Fedora