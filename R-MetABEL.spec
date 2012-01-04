%global packname  MetABEL
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          meta-analysis of genome-wide SNP association results

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid 

BuildRequires:    R-devel tex(latex) R-grid 

%description
a package for meta-analysis of genome-wide association scans between
quantitative or binary traits and SNPs

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
%doc %{rlibdir}/MetABEL/html
%doc %{rlibdir}/MetABEL/DESCRIPTION
%{rlibdir}/MetABEL/NAMESPACE
%{rlibdir}/MetABEL/Meta
%{rlibdir}/MetABEL/INDEX
%{rlibdir}/MetABEL/help
%{rlibdir}/MetABEL/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.3-1
- initial package for Fedora