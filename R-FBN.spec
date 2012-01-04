%global packname  FBN
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          FISH Based Normalization and Copy Number inference of SNP microarray data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Normalizes the data from a file containing the raw values of the SNP
probes of microarrray data by using the FISH probes and their
corresponding CNs.

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
%doc %{rlibdir}/FBN/DESCRIPTION
%doc %{rlibdir}/FBN/html
%{rlibdir}/FBN/data
%{rlibdir}/FBN/INDEX
%{rlibdir}/FBN/help
%{rlibdir}/FBN/Meta
%{rlibdir}/FBN/R
%{rlibdir}/FBN/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora