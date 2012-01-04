%global packname  LPE
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Methods for analyzing microarray data using Local Pooled Error (LPE) method

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This LPE library is used to do significance analysis of microarray data
with small number of replicates. It uses resampling based FDR adjustment,
and gives less conservative results than traditional 'BH' or 'BY'
procedures. Data accepted is raw data in txt format from MAS4, MAS5 or
dChip. Data can also be supplied after normalization. LPE library is
primarily used for analyzing data between two conditions. To use it for
paired data, see LPEP library. For using LPE in multiple conditions, use
HEM library.

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
%doc %{rlibdir}/LPE/DESCRIPTION
%doc %{rlibdir}/LPE/NEWS
%doc %{rlibdir}/LPE/doc
%doc %{rlibdir}/LPE/html
%{rlibdir}/LPE/Meta
%{rlibdir}/LPE/help
%{rlibdir}/LPE/R
%{rlibdir}/LPE/data
%{rlibdir}/LPE/NAMESPACE
%{rlibdir}/LPE/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora