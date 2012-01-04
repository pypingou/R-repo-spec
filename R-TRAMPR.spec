%global packname  TRAMPR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          TRFLP Analysis and Matching Package for R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
TRAMPR is an R package for matching terminal restriction fragment length
polymorphism (TRFLP) profiles between unknown samples and a database of
knowns.  TRAMPR facilitates analysis of many unknown profiles at once, and
provides tools for working directly with electrophoresis output through to
generating summaries suitable for community analyses with R's rich set of
statistical functions.  TRAMPR also resolves the issues of multiple TRFLP
profiles within a species, and shared TRFLP profiles across species.

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
%doc %{rlibdir}/TRAMPR/CITATION
%doc %{rlibdir}/TRAMPR/html
%doc %{rlibdir}/TRAMPR/doc
%doc %{rlibdir}/TRAMPR/DESCRIPTION
%{rlibdir}/TRAMPR/Meta
%{rlibdir}/TRAMPR/demo_samples_abi_template_full.csv
%{rlibdir}/TRAMPR/data
%{rlibdir}/TRAMPR/demo_samples_abi_info_full.csv
%{rlibdir}/TRAMPR/NAMESPACE
%{rlibdir}/TRAMPR/R
%{rlibdir}/TRAMPR/INDEX
%{rlibdir}/TRAMPR/help
%{rlibdir}/TRAMPR/demo_samples_abi.txt
%{rlibdir}/TRAMPR/demo_samples_abi_soilcore.csv

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora