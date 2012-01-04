%global packname  pvclust
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Hierarchical Clustering with P-Values via Multiscale Bootstrap Resampling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
pvclust is a package for assessing the uncertainty in hierarchical cluster
analysis. It provides AU (approximately unbiased) p-values as well as BP
(boostrap probability) values computed via multiscale bootstrap

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
%doc %{rlibdir}/pvclust/DESCRIPTION
%doc %{rlibdir}/pvclust/html
%{rlibdir}/pvclust/help
%{rlibdir}/pvclust/NAMESPACE
%{rlibdir}/pvclust/INDEX
%{rlibdir}/pvclust/Meta
%{rlibdir}/pvclust/R
%{rlibdir}/pvclust/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora