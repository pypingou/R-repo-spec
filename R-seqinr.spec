%global packname  seqinr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.0.5
Release:          1%{?dist}
Summary:          Biological Sequences Retrieval and Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Exploratory data analysis and data visualization for biological sequence
(DNA and protein) data. Include also utilities for sequence data
management under the ACNUC system.

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
%doc %{rlibdir}/seqinr/CITATION
%doc %{rlibdir}/seqinr/DESCRIPTION
%doc %{rlibdir}/seqinr/html
%{rlibdir}/seqinr/data
%{rlibdir}/seqinr/R
%{rlibdir}/seqinr/Meta
%{rlibdir}/seqinr/help
%{rlibdir}/seqinr/abif
%{rlibdir}/seqinr/INDEX
%{rlibdir}/seqinr/sequences
RPM build errors:
%{rlibdir}/seqinr/libs
%{rlibdir}/seqinr/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.0.5-1
- initial package for Fedora