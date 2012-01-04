%global packname  cytoDiv
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Cytometric diversity indices

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-GenKern R-plotrix 


BuildRequires:    R-devel tex(latex) R-GenKern R-plotrix



%description
Calculates ecological diversity indices for a microbial community

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
%doc %{rlibdir}/cytoDiv/DESCRIPTION
%doc %{rlibdir}/cytoDiv/html
%{rlibdir}/cytoDiv/NAMESPACE
%{rlibdir}/cytoDiv/Meta
%{rlibdir}/cytoDiv/extdata
%{rlibdir}/cytoDiv/INDEX
%{rlibdir}/cytoDiv/R
%{rlibdir}/cytoDiv/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.2-1
- initial package for Fedora