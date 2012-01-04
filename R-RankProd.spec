%global packname  RankProd
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.26.0
Release:          1%{?dist}
Summary:          Rank Product method for identifying differentially expressed genes with application in meta-analysis

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Non-paramteric method for identifying differentially expressed (up- or
down- regulated )genes based on the estimated percentage of false
predictions (pfp).The method can combine data sets from different origins
(meta-analysis)to increase the power of the identification.

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
%doc %{rlibdir}/RankProd/html
%doc %{rlibdir}/RankProd/DESCRIPTION
%doc %{rlibdir}/RankProd/doc
%{rlibdir}/RankProd/Meta
%{rlibdir}/RankProd/data
%{rlibdir}/RankProd/LICENSE
%{rlibdir}/RankProd/R
%{rlibdir}/RankProd/NAMESPACE
%{rlibdir}/RankProd/help
%{rlibdir}/RankProd/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.26.0-1
- initial package for Fedora