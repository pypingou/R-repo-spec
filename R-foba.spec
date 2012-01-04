%global packname  foba
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          greedy variable selection

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
foba is a package that implements forward, backward, and foba sparse
learning algorithms for ridge regression, described in the paper "Adaptive
Forward-Backward Greedy Algorithm for Learning Sparse Representations".

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
%doc %{rlibdir}/foba/DESCRIPTION
%doc %{rlibdir}/foba/html
%{rlibdir}/foba/help
%{rlibdir}/foba/INDEX
%{rlibdir}/foba/Meta
%{rlibdir}/foba/data
%{rlibdir}/foba/R
%{rlibdir}/foba/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora