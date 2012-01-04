%global packname  SASPECT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Significant AnalysiS of PEptide CounTs.

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A statistical method for significant analysis of comparative proteomics
based on LC-MS/MS Experiments

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
%doc %{rlibdir}/SASPECT/html
%doc %{rlibdir}/SASPECT/DESCRIPTION
%{rlibdir}/SASPECT/NAMESPACE
%{rlibdir}/SASPECT/Meta
%{rlibdir}/SASPECT/R
%{rlibdir}/SASPECT/data
%{rlibdir}/SASPECT/INDEX
%{rlibdir}/SASPECT/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora