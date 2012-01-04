%global packname  OrgMassSpecR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Organic Mass Spectrometry

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Organic/biological mass spectrometry data analysis.

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
%doc %{rlibdir}/OrgMassSpecR/html
%doc %{rlibdir}/OrgMassSpecR/doc
%doc %{rlibdir}/OrgMassSpecR/DESCRIPTION
%{rlibdir}/OrgMassSpecR/R
%{rlibdir}/OrgMassSpecR/NEWS.Rd
%{rlibdir}/OrgMassSpecR/LICENSE
%{rlibdir}/OrgMassSpecR/NAMESPACE
%{rlibdir}/OrgMassSpecR/Meta
%{rlibdir}/OrgMassSpecR/data
%{rlibdir}/OrgMassSpecR/help
%{rlibdir}/OrgMassSpecR/extdata
%{rlibdir}/OrgMassSpecR/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.5-1
- initial package for Fedora