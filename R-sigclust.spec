%global packname  sigclust
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Statistical Significance of Clustering

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
SigClust is a statistical method for testing the significance of
clustering results. SigClust can be applied to assess the statistical
significance of splitting a data set into two clusters. For more than two
clusters, SigClust can be used iteratively.

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
%doc %{rlibdir}/sigclust/html
%doc %{rlibdir}/sigclust/DESCRIPTION
%{rlibdir}/sigclust/R
%{rlibdir}/sigclust/NAMESPACE
%{rlibdir}/sigclust/help
%{rlibdir}/sigclust/INDEX
%{rlibdir}/sigclust/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora