%global packname  supclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Supervised Clustering of Predictor Variables such as Genes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Methodology for supervised grouping aka "clustering" of potentially many
predictor variables, such as genes etc.

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
%doc %{rlibdir}/supclust/DESCRIPTION
%doc %{rlibdir}/supclust/html
%{rlibdir}/supclust/help
%{rlibdir}/supclust/NAMESPACE
%{rlibdir}/supclust/data
%{rlibdir}/supclust/libs
%{rlibdir}/supclust/Meta
%{rlibdir}/supclust/R
%{rlibdir}/supclust/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora