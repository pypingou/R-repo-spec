%global packname  mclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.4.10
Release:          1%{?dist}
Summary:          Model-Based Clustering / Normal Mixture Modeling

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-stats R-utils 

%description
Model-based clustering and normal mixture modeling including Bayesian

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
%doc %{rlibdir}/mclust/html
%doc %{rlibdir}/mclust/DESCRIPTION
%doc %{rlibdir}/mclust/CITATION
%{rlibdir}/mclust/help
%{rlibdir}/mclust/libs
%{rlibdir}/mclust/INDEX
%{rlibdir}/mclust/data
%{rlibdir}/mclust/NAMESPACE
%{rlibdir}/mclust/cite
%{rlibdir}/mclust/Meta
RPM build errors:
%{rlibdir}/mclust/R
%{rlibdir}/mclust/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.4.10-1
- initial package for Fedora