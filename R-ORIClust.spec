%global packname  ORIClust
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Order-restricted Information Criterion-based Clustering Algorithm

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
ORIClust is a user-friendly R-based software package for gene clustering.
Clusters are given by genes matched to prespecified profiles across
various ordered treatment groups. It is particularly useful for analyzing
data obtained from short time-course or dose-response microarray

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
%doc %{rlibdir}/ORIClust/html
%doc %{rlibdir}/ORIClust/DESCRIPTION
%{rlibdir}/ORIClust/help
%{rlibdir}/ORIClust/NAMESPACE
%{rlibdir}/ORIClust/data
%{rlibdir}/ORIClust/Meta
%{rlibdir}/ORIClust/R
%{rlibdir}/ORIClust/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora