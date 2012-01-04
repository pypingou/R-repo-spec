%global packname  comorbidities
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Categorizes ICD-9-CM codes based on published comorbidity indices

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Methods to categorize ICD-9-CM codes into sensible disease categories have
been developed and published by numerous authors.  Two of the most widely
used such methods are the Deyo adaptation of the Charlson index and the
Elixhauser index. This package has functions to categorize comorbidites
into the Deyo-Charlson index, the original Elixhauser index of 30
comorbidities, and the AHRQ comorbidity index of 29 diagnoses (an update
to the original Elixhauser method).

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
%doc %{rlibdir}/comorbidities/DESCRIPTION
%doc %{rlibdir}/comorbidities/html
%{rlibdir}/comorbidities/INDEX
%{rlibdir}/comorbidities/Meta
%{rlibdir}/comorbidities/R
%{rlibdir}/comorbidities/help
%{rlibdir}/comorbidities/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora