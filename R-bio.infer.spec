%global packname  bio.infer
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.9
Release:          1%{?dist}
Summary:          Predict environmental conditions from biological observations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
Imports benthic count data, reformats this data, and computes
environmental inferences from this data.

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
%doc %{rlibdir}/bio.infer/DESCRIPTION
%doc %{rlibdir}/bio.infer/html
%{rlibdir}/bio.infer/data
%{rlibdir}/bio.infer/help
%{rlibdir}/bio.infer/NAMESPACE
%{rlibdir}/bio.infer/Meta
%{rlibdir}/bio.infer/R
%{rlibdir}/bio.infer/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.9-1
- initial package for Fedora