%global packname  dinamic
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          DiNAMIC A Method To Analyze Recurrent DNA Copy Number Aberrations in Tumors

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This function implements the DiNAMIC procedure for assessing the
statistical significance of recurrent DNA copy number aberrations
(Bioinformatics (2011) 27(5) 678 - 685).

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
%doc %{rlibdir}/dinamic/html
%doc %{rlibdir}/dinamic/DESCRIPTION
%{rlibdir}/dinamic/Meta
%{rlibdir}/dinamic/INDEX
%{rlibdir}/dinamic/NAMESPACE
%{rlibdir}/dinamic/help
%{rlibdir}/dinamic/data
%{rlibdir}/dinamic/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora