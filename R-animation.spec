%global packname  animation
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.5
Release:          1%{?dist}
Summary:          A Gallery of Animations in Statistics and Utilities to Create Animations

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains various functions for animations in statistics,
covering many areas such as probability theory, mathematical statistics,
multivariate statistics, nonparametric statistics, sampling survey, linear
models, time series, computational statistics, data mining and machine
learning. These functions might be of help in teaching statistics and data
analysis. Also provided in this package are several approaches to save
animations to various formats, e.g. Flash, GIF, HTML pages, PDF and videos
(saveSWF(), saveGIF(), saveHTML(), saveLatex(), and saveVideo()
respectively). PDF animations can be inserted into Sweave easily.

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
%doc %{rlibdir}/animation/DESCRIPTION
%doc %{rlibdir}/animation/html
%doc %{rlibdir}/animation/NEWS
%{rlibdir}/animation/data
%{rlibdir}/animation/demo
%{rlibdir}/animation/R
%{rlibdir}/animation/help
%{rlibdir}/animation/examples
%{rlibdir}/animation/Meta
%{rlibdir}/animation/misc
%{rlibdir}/animation/INDEX
%{rlibdir}/animation/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.5-1
- initial package for Fedora